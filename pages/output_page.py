def table_to_html(table_string):
    rows = table_string.split("\n")
    html = "<table>\n"
    for row in rows:
        html += "  <tr>\n"
        cols = row.split("\t")
        for col in cols:
            html += "    <td>" + col + "</td>\n"
        html += "  </tr>\n"
    html += "</table>"
    return html