KEY_PLAINTEXT = "aáàạảãăắằặẳẵâấầậẩẫbcdđeéẹẻẽêếềệểễfghiíìịỉĩjklmnoóòọỏõôốồộổỗơớờợởỡpqrstuúùụủũưứừựửữvwxyýỳỵỷỹAÁÀẠẢÃĂẮẰẶẲẴÂẤẦẬẨẪBCDĐEÉẸẺẼÊẾỀỆỂỄFGHIÍÌỊỈĨJKLMNOÓÒỌỎÕÔỐỒỘỔỖƠỚỜỢỞỠPQRSTUÚÙỤỦŨƯỨỪỰỬỮVWXYÝỲỴỶỸ0123456789`~!@#$%^&*()"

def encrypt(key, plaintext):
    reversedPlaintext = revertString(plaintext)

    result = ""

    for value in reversedPlaintext:

        textToOrd = (ord(value) + int(key)) %  len(KEY_PLAINTEXT)
        ordToText = chr(textToOrd)

        result += ordToText

    return result

def decrypt(key, plaintext):
    reversedPlaintext = revertString(plaintext)

    result = ""

    for value in reversedPlaintext:

        textToOrd = (ord(value) - int(key)) %  len(KEY_PLAINTEXT)
        ordToText = chr(textToOrd)

        result += ordToText

    return result

def revertString(plaintext):
    result = ""
    totalLen = len(plaintext) - 1

    for value in range(totalLen , -1, -1):
        result += plaintext[value]

    return result

def stringFormatted(plaintext):
    lowerPlaintext = plaintext.lower()
    noSpacePlaintext = "".join(lowerPlaintext.split())

    return noSpacePlaintext

def main():
    inputPlaintext = input("Enter phrase to Encrypt (lowercase, no spaces): ")
    distance = input("Enter distance value: ")

    plaintextFormatted = stringFormatted(inputPlaintext)
    print(encrypt(distance, plaintextFormatted))

    inputPlaintext = input("Enter phrase to Decrypt (lowercase, no spaces): ")
    distance = input("Enter distance value: ")

    plaintextFormatted = stringFormatted(inputPlaintext)
    print(decrypt(distance, plaintextFormatted))
