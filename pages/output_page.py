def table_to_html(table_string):
    rows = table_string.split("\n")
    html = "<table border='1'>\n"
    for i, row in enumerate(rows):
        if i % 2 == 0:
            bg_color = ""
        else:
            bg_color = "background-color: #f2f2f2;"
        html += "  <tr style='" + bg_color + "'>\n"
        cols = row.split("\t")
        for col in cols:
            html += "    <td style='border: 1px solid black;'>" + col + "</td>\n"
        html += "  </tr>\n"
    html += "</table>"
    return html