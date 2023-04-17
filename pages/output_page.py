def table_to_html(table_string):
    rows = table_string.split("\n")
    html = "<table>\n"
    for i, row in enumerate(rows):
        if i % 2 == 1:
            bg_color = ""
        else:
            bg_color = "background-color: #f2f2f2;"
        if i == 0:
            bg_color = "background-color: #e2e2e2;"
        html += "  <tr style='" + bg_color + "'>\n"
        cols = row.split("\t")
        for col in cols:
            html += "    <td>" + col + "</td>\n"
        html += "  </tr>\n"
    html += "</table>"
    return html