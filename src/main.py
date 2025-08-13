import boto3

def save_file_to_s3(bucket_name, file_name, content):
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=content)
    print(f"File '{file_name}' saved to bucket '{bucket_name}'.")

def main():
    bucket_name = "my-python-app-bucket"  # Update if needed
    file_name = "example.txt"
    content = "Hello from My Python App!"
    save_file_to_s3(bucket_name, file_name, content)

if __name__ == "__main__":
    main()