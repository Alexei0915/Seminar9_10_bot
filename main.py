from telegram import Update
from telegram.ext import  CommandHandler,ApplicationBuilder,ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("*****************************************MwTs2B*********ZA8").build()
app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('help', help_command))
app.add_handler(CommandHandler('sum', mat_operations_command))
app.add_handler(CommandHandler('mult', mat_operations_command ))
app.add_handler(CommandHandler('divis', mat_operations_command ))
app.add_handler(CommandHandler('sub', mat_operations_command ))

print('server start')
app.run_polling()


