import modal

app = modal.App("ai-resume-reviewer")

image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install_from_requirements("requirements.txt")
    .add_local_dir(".", remote_path="/root/app")
)

@app.function(
    image=image,
    secrets=[
        modal.Secret.from_name("groq-secret")
    ],
)
@modal.asgi_app()
def web():
    import os
    import sys
    import gradio as gr
    from fastapi import FastAPI

    os.chdir("/root/app")
    sys.path.insert(0, "/root/app")

    from ui.gradio_app import demo

    app = FastAPI()

    app = gr.mount_gradio_app(
        app,
        demo,
        path="/"
    )

    return app