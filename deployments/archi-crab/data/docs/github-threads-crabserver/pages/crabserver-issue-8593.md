# dmwm/CRABServer issue #8593: add exit code 10040 (and others) to list of recoverable errors

State: open
Opened: 2024-08-07T13:38:26Z
Labels: Type: Enhancement, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/8593

## Opening post (belforte, 2024-08-07T13:38:26Z)

currently we only retry this
https://github.com/dmwm/CRABServer/blob/6852e951c6c661e7290ea58ed9cb03ec69c56ace/src/python/TaskWorker/Actions/RetryJob.py#L381-L384
but there are many other possible exit codes which signal very high likelyhood of site error and are worth retrying in [the twiki](https://twiki.cern.ch/twiki/bin/view/CMSPublic/JobExitCodes) [1]

even if some of those are now obsolete (i.e. we do not have code which could rise them in our JobWrapper anymore)

[1]
possibe site-related error are marked with the attention sign :
![image](https://github.com/user-attachments/assets/dff040bf-747d-4c61-b1d7-50917c4fc6a4)


reference: https://cms-talk.web.cern.ch/t/strange-error-on-crab-site-misconfiguration/45226/3

## Comment (aspiringmind-code, 2024-08-07T14:41:09Z)

@belforte Should I have a separate message for each of the site errors or can I club some of the errors, say for exit codes 60315, 60321, 60311, we can have the same error message called "Site Error:Stage-out related troubles"

## Comment (belforte, 2024-08-07T14:59:57Z)

for the time being you should simply add this to the list and put it at 
lower priority than the other things.

I need to check where we use that message !

On 07/08/2024 16:41, aspiringmind-code wrote:
>
> @belforte <https://github.com/belforte> Should I have a separate 
> message for each of the site errors or can I club some of the errors, 
> say for exit codes 60315, 60321, 60311, we can have the same error 
> message called "Site Error:Stage-out related troubles"
>
> —
> Reply to this email directly, view it on GitHub 
> <https://github.com/dmwm/CRABServer/issues/8593#issuecomment-2273642592>, 
> or unsubscribe 
> <https://github.com/notifications/unsubscribe-auth/AAOAVWOE7ALI25LZXN7DHBDZQIWZXAVCNFSM6AAAAABMEOGOHSVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDENZTGY2DENJZGI>.
> You are receiving this because you were mentioned.Message ID: 
> ***@***.***>
>
--------------DSh4rWnQkVnstMjKuWxf3Coh
Content-Type: text/html; charset=UTF-8
Content-Transfer-Encoding: 8bit

<!DOCTYPE html><html><head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  </head>
  <body>
    <p>for the time being you should simply add this to the list and put
      it at lower priority than the other things.</p>
    <p>I need to check where we use that message !<br>
    </p>
    <div class="moz-cite-prefix">On 07/08/2024 16:41, aspiringmind-code
      wrote:<br>
    </div>
    <blockquote type="cite" ***@***.***">
      
      <p dir="auto"><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/belforte/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/belforte" ***@***.***</a>
        Should I have a separate message for each of the site errors or
        can I club some of the errors, say for exit codes 60315, 60321,
        60311, we can have the same error message called &quot;Site
        Error:Stage-out related troubles&quot;</p>
      <p style="font-size:small;-webkit-text-size-adjust:none;color:#666;">—<br>
        Reply to this email directly, <a href="https://github.com/dmwm/CRABServer/issues/8593#issuecomment-2273642592" moz-do-not-send="true">view it on GitHub</a>, or <a href="https://github.com/notifications/unsubscribe-auth/AAOAVWOE7ALI25LZXN7DHBDZQIWZXAVCNFSM6AAAAABMEOGOHSVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDENZTGY2DENJZGI" moz-do-not-send="true">unsubscribe</a>.<br>
        You are receiving this because you were mentioned.<img src="https://github.com/notifications/beacon/AAOAVWJ44SVDOG3XTENIFELZQIWZXA5CNFSM6AAAAABMEOGOHSWGG33NNVSW45C7OR4XAZNMJFZXG5LFINXW23LFNZ2KUY3PNVWWK3TUL5UWJTUHQUEGA.gif" alt="" moz-do-not-send="true" width="1" height="1"><span style="color: transparent; font-size: 0; display: none; visibility: hidden; overflow: hidden; opacity: 0; width: 0; height: 0; max-width: 0; max-height: 0; mso-hide: all">Message
          ID: <span>&lt;dmwm/CRABServer/issues/8593/2273642592</span><span>@</span><span>github</span><span>.</span><span>com&gt;</span></span></p>
      <script type="application/ld+json">[
{
***@***.***": "http://schema.org",
***@***.***": "EmailMessage",
"potentialAction": {
***@***.***": "ViewAction",
"target": "https://github.com/dmwm/CRABServer/issues/8593#issuecomment-2273642592",
"url": "https://github.com/dmwm/CRABServer/issues/8593#issuecomment-2273642592",
"name": "View Issue"
},
"description": "View this Issue on GitHub",
"publisher": {
***@***.***": "Organization",
"name": "GitHub",
"url": "https://github.com"
}
}
]</script>
    </blockquote>
  </body>
</html>

--------------DSh4rWnQkVnstMjKuWxf3Coh--

## Comment (belforte, 2026-07-13T14:24:55Z)

now that we have new job retry code, it is time to review our exit code handling
