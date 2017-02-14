# -*- coding: UTF-8 -*-
from flask import *
from flask_mail import Message
from app import mail
from app.main import main


@main.route('/mail/')
def sendmail():
    msg = Message('test mail', recipients=[''])
    mail.send(msg)
    return jsonify({'status': 0})


@main.route('/mailto', methods=['POST'])
def sendmailto():
    if request.method == 'POST':
        json_result = request.get_json(force=True)
        title = json_result['title']
        content = json_result['content']
        recipients = [json_result['recipients'], ]
        msg = Message(title, recipients=recipients, body=content)
        mail.send(msg)
        return jsonify({'status': 0})
    else:
        return jsonify({'status': 1})

#todo 大量邮件
# with mail.connect() as conn:
#     for user in users:
#         message = '...'
#         subject = "hello, %s" % user.name
#         msg = Message(recipients=[user.email],
#                       body=message,
#                       subject=subject)
#
#         conn.send(msg)

#todo 附件
# with app.open_resource("image.png") as fp:
#     msg.attach("image.png", "image/png", fp.read())