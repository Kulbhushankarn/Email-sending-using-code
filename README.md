# Email-sending-using-code
Sending the email using python.
*3 ways to send emails from your Python app*
There are three main options for sending email with Python: SMTP, a transactional email service, and a multichannel notifications service.

Below, I’ll review the pros and cons for each option. Then, in the next section, I’ll walk you through three different code tutorials for using each option to send emails with Python.

# 1. Using SMTP
Python has a built-in module for sending emails via SMTP, which makes getting started with email a piece of cake.

Pros of using SMTP
Easy to set up

Highly cost-effective

Platform agnostic

Cons of using SMTP
Less secure

No built-in analytics

Longer send times

Long-term maintenance and uptime burden

# 2. Using a transactional email service
You can also easily integrate third-party transactional email APIs like SendGrid, Mailgun, and AWS SES. If you are planning to send a high volume of emails or need to ensure deliverability, a hosted email API can be a great option and many providers offer a free or low-cost plan to start.

Pros of transactional email services
Feature-rich, e.g. analytics
High email delivery rates
Better email delivery speeds
Scalability and reliability



Cons of transactional email services
Learning curve for new API

Dependent on third-party intermediary

# 3. Using a multichannel notifications service
Finally, if you’re planning to notify users on more than one channel, you can use a multichannel notifications service. Courier, for example, gives you one uniform API to notify users over email, SMS, push, and chat apps like Slack and WhatsApp. Plus, you’ll get a drag-and-drop template builder and real-time logs and analytics for all your channels.

Even if you’re only sending emails today, multichannel notifications services can save you time and money. With a platform like Courier, you can easily add new channels, switch email service providers, or even add backup providers without writing any additional code. You get a complete notifications system that can scale with your product’s growth.

Pros of multichannel notifications services
Single API for multiple channels

Easy to manage cross-channel delivery

Less code to write and maintain

Cons of multichannel notifications services
Additional third-party intermediary

# Tutorial: How to send emails using SMTP in Python
You can use Python’s built-in `smtplib` module to send email using SMTP (Simple Mail Transfer Protocol), which is an application-level protocol. Note that the module makes use of RFC 821 protocol for SMTP. I’ll show you how to use Gmail’s SMTP server for this walkthrough. 

1. Set up a Gmail account for sending your emails. Since you’ll be feeding a plaintext password to the program, Google considers the SMTP connection less secure. 

2. Go to the account settings and allow *less secure apps* to access the account. As an aside, Gmail doesn't necessarily use SMTP on their internal mail servers; however, Gmail SMTP is an interface enabled by Google's smtp.gmail.com server. You might find smtp.gmail.com in email clients like Thunderbird, Outlook, and others.

3. Import `smtplib`. Since Python comes pre-packaged with `smtplib`, all you have to do is create a Python file and import `smtplib` into it. 

4. To create a secure connection, you can either use `SMTP_SSL()` with 465 port or `.starttls()` with 587 port. The former creates an SMTP connection that is secured from the beginning. The latter creates an unsecured SMTP connection that is encrypted via `.starttls()`.

To send email through `SMTP_SSL()`:



