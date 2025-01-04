import matplotlib
matplotlib.use('Agg')  # Make sure this is at the very top
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import sqlite3
import re
import requests
import csv
from datetime import datetime
import io
import base64
from bcrypt import hashpw, gensalt, checkpw


app = Flask(__name__)
app.secret_key = "your_secret_key"
