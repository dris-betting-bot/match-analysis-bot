#!/usr/bin/env python3
"""
Match Analysis Betting Bot for Telegram
Analyzes football matches and provides predictions
"""

import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import requests
from datetime import datetime
from analyzer import MatchAnalyzer

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Configuration
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', '8834948528:AAGYNH4TQZE2ve3bSw007QaXNoxCJYpJr-o')
FOOTBALL_API_KEY = os.getenv('FOOTBALL_API_KEY', 'ba15271bc79f4a01a4ddae95a017ad72')
FOOTBALL_API_BASE = 'https://api.football-data.org/v4'

analyzer = MatchAnalyzer(FOOTBALL_API_KEY)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Start command handler"""
    welcome_message = """
🤖 *مرحبا بك في بوت تحليل المباريات!* ⚽

أنا هنا لتحليل المباريات وإعطائك التوقعات الدقيقة.

📋 *كيفية الاستخدام:*
أرسل لي اسم الفريقين والتاريخ:
• مثال: ريال مدريد vs برشلونة - 25 نونبر
• أو: LA Galaxy vs Colorado Rapids

🎯 *ماذا سأحصل عليه:*
✅ توقع النتيجة (فوز/تعادل/خسارة) مع النسبة المئوية
✅ تحليل الإصابات والغيابات
✅ أداء الفريق في البيت والخارج
✅ توقع Over/Under مع النسبة المئوية
✅ تحليل الركنيات المتوقعة
✅ الإحصائيات الهجومية والدفاعية

🚀 *ابدأ الآن! أرسل اسم المباراة*
    """
    await update.message.reply_text(welcome_message, parse_mode='Markdown')

async def analyze_match(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle match analysis requests"""
    try:
        user_message = update.message.text
        
        # Show loading message
        loading_msg = await update.message.reply_text("⏳ جاري البحث عن المباراة وتحليلها...")
        
        # Analyze the match
        result = await analyzer.analyze_match_query(user_message)
        
        if result['success']:
            analysis = result['analysis']
            
            # Format the response
            response = format_analysis_response(analysis)
            
            await loading_msg.edit_text(response, parse_mode='Markdown')
        else:
            error_message = f"❌ {result['error']}\n\n💡 تأكد من كتابة أسماء الفريقين بشكل صحيح."
            await loading_msg.edit_text(error_message)
            
    except Exception as e:
        logger.error(f"Error analyzing match: {e}")
        await update.message.reply_text(f"❌ حدث خطأ: {str(e)}")

def format_analysis_response(analysis: dict) -> str:
    """Format analysis results for Telegram"""
    response = f"""
🏆 *تحليل المباراة*

📊 *المباراة:* {analysis.get('match_name', 'N/A')}
📅 *التاريخ:* {analysis.get('date', 'N/A')}

━━━━━━━━━━━━━━━━━━

*🎯 توقع النتيجة:*
• 🔵 فوز الفريق الأول: {analysis['prediction'].get('team1_win', 0):.1f}%
• ⚪ تعادل: {analysis['prediction'].get('draw', 0):.1f}%
• 🔴 فوز الفريق الثاني: {analysis['prediction'].get('team2_win', 0):.1f}%

━━━━━━━━━━━━━━━━━━

*⚽ الأهداف المتوقعة:*
• مجموع الأهداف المتوقع: {analysis['goals'].get('total', 0):.1f}
• Over 2.5: {analysis['goals'].get('over_2_5', 0):.1f}%
• Under 2.5: {analysis['goals'].get('under_2_5', 0):.1f}%
• Over 3.5: {analysis['goals'].get('over_3_5', 0):.1f}%
• Under 3.5: {analysis['goals'].get('under_3_5', 0):.1f}%

━━━━━━━━━━━━━━━━━━

*📈 إحصائيات الفريقين:*

{analysis['stats'].get('team1_name', 'الفريق 1')}:
• متوسط الأهداف: {analysis['stats'].get('team1_avg_goals', 0):.2f}
• متوسط الاستقبال: {analysis['stats'].get('team1_avg_conceded', 0):.2f}
• الأداء في البيت: {analysis['stats'].get('team1_home_form', 'N/A')}

{analysis['stats'].get('team2_name', 'الفريق 2')}:
• متوسط الأهداف: {analysis['stats'].get('team2_avg_goals', 0):.2f}
• متوسط الاستقبال: {analysis['stats'].get('team2_avg_conceded', 0):.2f}
• الأداء خارج الديار: {analysis['stats'].get('team2_away_form', 'N/A')}

━━━━━━━━━━━━━━━━━━

*🚩 الركنيات المتوقعة:*
• عدد الركنيات: {analysis['corners'].get('expected_corners', 0):.0f}
• الفريق 1: {analysis['corners'].get('team1_corners', 0):.0f}
• الفريق 2: {analysis['corners'].get('team2_corners', 0):.0f}

━━━━━━━━━━━━━━━━━━

*⚠️ ملاحظات هامة:*
{analysis['notes']}

⭐ *تحليل من بوت تحليل المباريات الذكي*
    """
    return response

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Help command"""
    help_text = """
📚 *مساعدة البوت*

*الأوامر المتاحة:*
/start - البدء والترحيب
/help - هذه الرسالة
/about - معلومات عن البوت

*كيفية الاستخدام:*
ببساطة، أرسل لي:
✍️ اسم الفريق الأول
✍️ vs أو مقابل
✍️ اسم الفريق الثاني
✍️ التاريخ (اختياري)

*أمثلة:*
• ريال مدريد vs برشلونة
• Bayern Munich vs Dortmund - 15 أكتوبر
• Manchester United vs Liverpool

🤖 البوت سيحلل كل شيء تلقائياً!
    """
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """About command"""
    about_text = """
ℹ️ *عن البوت*

🎯 *الهدف:* تحليل المباريات الرياضية بذكاء وإعطاء توقعات دقيقة

📊 *المميزات:*
• تحليل إحصائي متقدم للمباريات
• توقعات دقيقة للنتائج والأهداف
• تحليل أداء الفريقين في البيت والخارج
• متابعة الإصابات والغيابات
• تحليل الركنيات والبيانات المتقدمة

🔧 *التقنيات:*
• Python + Telegram API
• Football Data API
• Machine Learning للتنبؤ

👨‍💻 *المطور:* Dris Betting Bot
📧 *البريد:* support@dris.bot

🚀 *الإصدار:* 1.0.0

⭐ استمتع بالتحليلات الدقيقة!
    """
    await update.message.reply_text(about_text, parse_mode='Markdown')

def main() -> None:
    """Start the bot"""
    # Create the Application
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about_command))
    
    # Handle text messages (match analysis requests)
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, 
        analyze_match
    ))

    # Run the bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
