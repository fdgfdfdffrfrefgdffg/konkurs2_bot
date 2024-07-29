from aiogram.types import Message, FSInputFile
import data

async def get_stat(message: Message):
    stat = data.get_stats()
    text = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Statistika</title>
    <style>
        table{
            width: 100%;
            border: 2px solid black;
        }
        thead{
            background-color: rgb(146, 101, 11);
            color: white;
        }
        tbody{
            background-color: rgb(233, 190, 104);
        }
    </style>
</head>
<body>
    <table>
        <thead>
            <tr>
                <th>O'rin</th>
                <th>Ism-familya</th>
                <th>Telefon raqam</th>
                <th>Notcoin</th>
            </tr>
        </thead>
        <tbody>
"""
    r = 1
    for i in stat:
        user = data.get_user(i[0])
        if user and user.status == 1:
            text += f"<tr><td>{r}</td><td>{user.name}</td><td>{user.phone}</td><td>{i[1]}<td>"
            r += 1
    text += """
        </tbody>
    </table>
</body>
</html>
"""
    with open("statistika.html", "w") as html_doc:
        html_doc.write(text)
    users = data.get_users()

    await message.answer_document(FSInputFile("statistika.html"), caption=f"Bu yerda {r} ta foydalanuvchi bo'yicha statistika mavjud!\n\nUmumiy foydalanuvchilar soni: {len(users)} ta",)
    