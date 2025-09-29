def otp_sms(name, otp):
    return f"""
سلام {name} عزیز، به لووپ خوش آمدید!

رمز یکبار مصرف شما: {otp}
CODE: {otp}

این یک پیام محرمانه برای شماست؛ در اختیار دیگران قرار ندهید.
lloop.ir/home
    """

def request_customer_sms(product_name, request_code, request_count, shop_name):
    return f"""
درخواست شما با موفقیت ثبت شد.

محصول {product_name} به تعداد {request_count} از فروشگاه {shop_name}
کد درخواست: {request_code}

lloop.ir/dashboard/requests
    """

def request_vendors_sms(product_name, request_code, request_count):
    return f"""
درخواست جدیدی برای شما ثبت شد.

محصول {product_name} به تعداد {request_count}
کد درخواست: {request_code}

lloop.ir/dashboard/requests
    """