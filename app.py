from flask import Flask, render_template, request, redirect, send_file

app=Flask(__name__)

@app.route('/')
def main():
    return  render_template('index.html')