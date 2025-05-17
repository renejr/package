import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import mm

def _parse_messages(json_data):
    # Aceita lista de mensagens ou dicionário com chave 'messages'
    if isinstance(json_data, dict) and 'messages' in json_data:
        messages = json_data['messages']
    elif isinstance(json_data, list):
        messages = json_data
    else:
        messages = []
    # Normaliza campos
    parsed = []
    for msg in messages:
        author = msg.get('author', msg.get('Author', msg.get('user', 'Desconhecido')))
        timestamp = msg.get('timestamp', msg.get('Timestamp', msg.get('date', '')))
        content = msg.get('content', msg.get('Contents', msg.get('message', '')))
        attachments = msg.get('attachments', msg.get('Attachments', ''))
        # attachments pode ser lista ou string
        if isinstance(attachments, str):
            attachments = [a.strip() for a in attachments.split(',') if a.strip()]
        elif not isinstance(attachments, list):
            attachments = []
        parsed.append({
            'author': author,
            'timestamp': timestamp,
            'content': content,
            'attachments': attachments
        })
    return parsed

def json_to_html(json_data):
    messages = _parse_messages(json_data)
    html = [
        '<!DOCTYPE html>',
        '<html lang="pt-br">',
        '<head>',
        '<meta charset="UTF-8">',
        '<title>Exportação Chat Discord</title>',
        '<style>',
        'body { background: #36393f; color: #dcddde; font-family: Arial, sans-serif; margin: 0; padding: 0; }',
        '.chat { max-width: 800px; margin: 30px auto; padding: 20px; background: #2f3136; border-radius: 8px; }',
        '.msg { margin-bottom: 18px; padding: 10px 15px; border-radius: 8px; background: #40444b; position: relative; }',
        '.author { font-weight: bold; color: #fff; }',
        '.timestamp { color: #b9bbbe; font-size: 0.9em; margin-left: 8px; }',
        '.content { margin: 6px 0 0 0; white-space: pre-wrap; }',
        '.attachments { margin-top: 8px; }',
        '.attachment-link { color: #00b0f4; text-decoration: underline; }',
        '</style>',
        '</head>',
        '<body>',
        '<div class="chat">'
    ]
    for msg in messages:
        html.append('<div class="msg">')
        html.append(f'<span class="author">{msg["author"]}</span>')
        if msg["timestamp"]:
            html.append(f'<span class="timestamp">{msg["timestamp"]}</span>')
        html.append(f'<div class="content">{msg["content"]}</div>')
        if msg["attachments"]:
            html.append('<div class="attachments">')
            for att in msg["attachments"]:
                if att.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    html.append(f'<img src="{att}" alt="imagem" style="max-width:300px; display:block; margin-top:5px;">')
                else:
                    html.append(f'<a class="attachment-link" href="{att}">{att}</a>')
            html.append('</div>')
        html.append('</div>')
    html.append('</div></body></html>')
    return '\n'.join(html)

def json_to_md(json_data):
    messages = _parse_messages(json_data)
    md = []
    for msg in messages:
        line = f'**{msg["author"]}**'
        if msg["timestamp"]:
            line += f' _({msg["timestamp"]})_'
        md.append(line)
        md.append(f'> {msg["content"]}')
        if msg["attachments"]:
            for att in msg["attachments"]:
                if att.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    md.append(f'![imagem]({att})')
                else:
                    md.append(f'[Anexo]({att})')
        md.append('')  # linha em branco entre mensagens
    return '\n'.join(md)

def json_to_pdf(json_data, output_path):
    messages = _parse_messages(json_data)
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4
    margin = 20 * mm
    y = height - margin
    chat_width = width - 2 * margin

    def draw_rounded_box(x, y, w, h, r, fill_color):
        c.setFillColor(fill_color)
        c.roundRect(x, y, w, h, r, fill=1, stroke=0)

    def draw_msg(author, timestamp, content, attachments):
        nonlocal y
        # Medidas do balão
        box_padding = 6
        line_height = 13
        max_content_width = chat_width - 2 * box_padding
        # Calcular altura do conteúdo
        content_lines = content.splitlines() or [""]
        n_lines = len(content_lines)
        n_attach = len(attachments) if attachments else 0
        box_height = (n_lines + n_attach) * line_height + 32

        if y - box_height < margin:
            c.showPage()
            c.setFillColor(colors.HexColor("#2f3136"))
            c.rect(0, 0, width, height, fill=1)
            y = height - margin

        # Balão de mensagem
        box_y = y - box_height
        draw_rounded_box(margin, box_y, chat_width, box_height, 8, colors.HexColor("#40444b"))

        # Nome e timestamp
        c.setFont("Helvetica-Bold", 11)
        c.setFillColor(colors.white)
        c.drawString(margin + box_padding, y - 18, author)
        c.setFont("Helvetica", 8)
        c.setFillColor(colors.HexColor("#b9bbbe"))
        c.drawString(margin + box_padding + 120, y - 18, timestamp)

        # Conteúdo
        c.setFont("Helvetica", 10)
        c.setFillColor(colors.white)
        text_y = y - 32
        for line in content_lines:
            c.drawString(margin + box_padding, text_y, line)
            text_y -= line_height

        # Anexos
        if attachments:
            c.setFont("Helvetica-Oblique", 9)
            c.setFillColor(colors.HexColor("#00b0f4"))
            for att in attachments:
                if att.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    c.drawString(margin + box_padding, text_y, f"[imagem] {att}")
                else:
                    c.drawString(margin + box_padding, text_y, f"[anexo] {att}")
                text_y -= line_height

        y -= box_height + 8  # Espaço entre mensagens

    # Fundo escuro
    c.setFillColor(colors.HexColor("#2f3136"))
    c.rect(0, 0, width, height, fill=1)
    y -= 10
    for msg in messages:
        draw_msg(msg["author"], msg["timestamp"], msg["content"], msg["attachments"])
    c.save()