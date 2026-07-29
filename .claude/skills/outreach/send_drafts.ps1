<#
.SYNOPSIS
  Creates (or sends) a whole outreach batch in Outlook from send-batch.csv in one run,
  instead of opening each .eml by hand.

.DESCRIPTION
  Reads contract-manufacturing/outreach-drafts/<batch>/send-batch.csv, which
  outreach_build.py writes alongside the .eml files. For each row it builds a real
  Outlook mail item, appends your normal Outlook signature underneath the body, and
  either saves it to Drafts (default) or sends it.

  Requires: Windows, Outlook desktop, signed in. Outlook must be running or it will
  be started. Nothing here touches the network directly - Outlook does the sending,
  so the mail goes out through your HBS account exactly as if you had clicked Send.

.PARAMETER Csv
  Path to send-batch.csv.

.PARAMETER Send
  Send immediately. Without it, every message is saved to Drafts for review.

.PARAMETER DelaySeconds
  Pause between sends. Default 20. Only used with -Send. Keeps a 50-message batch
  spread over ~17 minutes so it does not look like a blast to the mail filters.

.PARAMETER Limit
  Stop after N rows. Use for a first test run.

.EXAMPLE
  # dry run - see what would happen, create nothing
  .\send_drafts.ps1 -Csv .\contract-manufacturing\outreach-drafts\2026-07-30\send-batch.csv -WhatIf

.EXAMPLE
  # create all as drafts, review in Outlook, send by hand
  .\send_drafts.ps1 -Csv .\contract-manufacturing\outreach-drafts\2026-07-30\send-batch.csv

.EXAMPLE
  # send the first 3 as a live test, then the rest
  .\send_drafts.ps1 -Csv .\...\send-batch.csv -Send -Limit 3
#>
[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [Parameter(Mandatory = $true)][string]$Csv,
    [switch]$Send,
    [int]$DelaySeconds = 20,
    [int]$Limit = 0
)

$ErrorActionPreference = 'Stop'

if (-not (Test-Path $Csv)) { throw "No such file: $Csv" }
$rows = Import-Csv -Path $Csv
if ($Limit -gt 0) { $rows = $rows | Select-Object -First $Limit }
if (-not $rows) { throw "$Csv has no rows" }

Write-Host ("{0} message(s) from {1}" -f $rows.Count, $Csv)
Write-Host ($(if ($Send) { "Mode: SEND (delay ${DelaySeconds}s)" } else { "Mode: SAVE TO DRAFTS" })) -ForegroundColor Yellow

$outlook = New-Object -ComObject Outlook.Application

$log = [System.Collections.Generic.List[object]]::new()
$i = 0
foreach ($r in $rows) {
    $i++
    $label = "{0}/{1}  {2} <{3}>" -f $i, $rows.Count, $r.Contact, $r.To

    if (-not $PSCmdlet.ShouldProcess($r.To, $(if ($Send) { 'Send' } else { 'Save draft' }))) {
        Write-Host "  [skipped by -WhatIf] $label"; continue
    }

    try {
        $mail = $outlook.CreateItem(0)          # olMailItem
        $mail.To = $r.To
        if ($r.Cc) { $mail.CC = $r.Cc }
        $mail.Subject = $r.Subject

        # Touching the inspector makes Outlook drop your default signature into
        # HTMLBody. Capture it, then put our body above it - otherwise assigning
        # HTMLBody wipes the signature and the mail arrives unsigned.
        $null = $mail.GetInspector
        $signature = $mail.HTMLBody
        $mail.HTMLBody = $r.HtmlBody + $signature

        if ($Send) {
            $mail.Send()
            Write-Host "  sent     $label" -ForegroundColor Green
            $status = 'sent'
            if ($i -lt $rows.Count) { Start-Sleep -Seconds $DelaySeconds }
        }
        else {
            $mail.Save()                        # lands in Drafts
            Write-Host "  drafted  $label"
            $status = 'drafted'
        }
    }
    catch {
        Write-Host "  FAILED   $label  -  $($_.Exception.Message)" -ForegroundColor Red
        $status = "failed: $($_.Exception.Message)"
    }

    $log.Add([pscustomobject]@{
            Company = $r.Company; Contact = $r.Contact; To = $r.To
            Status  = $status; Timestamp = (Get-Date).ToString('s')
        })
}

$logPath = Join-Path (Split-Path -Parent $Csv) 'send-log.csv'
$log | Export-Csv -Path $logPath -NoTypeInformation -Encoding UTF8
Write-Host "`nLog: $logPath" -ForegroundColor Cyan
Write-Host "Paste that file back into the session and the tracker gets updated from it."
