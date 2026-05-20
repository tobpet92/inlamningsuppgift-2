def lambda_handler(event, context):
    html = """
    <!DOCTYPE html>
    <html>
    <head><title>Min Serverless App</title></head>
    <body>
      <h1>Hej från AWS Lambda!</h1>
      <p>Den här sidan körs serverless – ingen server behövs!</p>
    </body>
    </html>
    """
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html"
        },
        "body": html
    }