#!/usr/bin/env python3
"""
Email generator and sender.
"""

import email.message
import mimetypes
import smtplib
import os


def build_email(sender, recipient, subject, body, attachment_path):
    """Create an email with an optional attachment."""
    msg = email.message.EmailMessage()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.set_content(body)

    if attachment_path:
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split("/")

        with open(attachment_path, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype=mime_type,
                subtype=mime_subtype,
                filename=os.path.basename(attachment_path)
            )

    return msg


def send_email(message, smtp_server="localhost"):
    """Send an email via local SMTP."""
    with smtplib.SMTP(smtp_server) as server:
        server.send_message(message)
