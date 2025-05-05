# ---- Stage 1: Build and install everything securely ----
FROM python:3.10-slim as builder

WORKDIR /app
COPY . .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir flask scikit-learn numpy && \
    pip freeze > requirements.txt

# ---- Stage 2: Use Chainguard Python securely with working libs ----
FROM cgr.dev/chainguard/python:latest

WORKDIR /app
COPY --from=builder /app /app

# Copy compiled Python dependencies
COPY --from=builder /usr/local/lib/python3.10 /usr/local/lib/python3.10
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /usr/local/lib/libpython3.10.so.1.0 /usr/local/lib/libpython3.10.so.1.0


# Make sure /usr/local/bin is in PATH (for python, pip, etc.)
ENV PATH="/usr/local/bin:$PATH"

EXPOSE 5001
EXPOSE 5002
EXPOSE 5003

ENTRYPOINT ["python"]
CMD ["main.py"]
