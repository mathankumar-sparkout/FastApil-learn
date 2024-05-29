from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr
from jinja2 import Template

app = FastAPI()

conf = ConnectionConfig(
    MAIL_USERNAME="polkabull@gmail.com",
    MAIL_PASSWORD="kjrpodkeckdinkzf",
    MAIL_FROM="mathankumar@sparkouttech.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
)


def render_template() -> str: 
    template_path = "templates\index.html"

    with open(template_path) as file:    #index.html file
        template_content = file.read()    #read the content
        template = Template(template_content)  #inherit the all content use jinja template
        body_data = {
            "title": "Email Title",  
            "message": "Hello, this is the email content!",
        }
    return template.render(body_data) # html file inherit body_data


#email 
async def send_email(email_to: EmailStr): 
    rendered_body = render_template()
    message = MessageSchema(
        subject="Email Subject",
        recipients=[email_to],
        body=rendered_body,
        subtype="html",
    )
    fm = FastMail(conf)
    await fm.send_message(message)


@app.post("/send-email")
async def send_email_route(email: EmailStr):
    await send_email(email)  # docs loading few sec using await and throw msg return
    return {"message": "Email sent successfully"}
