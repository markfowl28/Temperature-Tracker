import base64
from io import BytesIO
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

def find_data(mysql, month, day):
    cursor = mysql.connection.cursor()
    cursor.execute("select temp, hour from temperature_tracker where day = %s and month = %s", (day, month))
    result = cursor.fetchall()

    temp = []
    hour = []

    for i in result:
        temp.append(i[0])
        hour.append(i[1])
    
    cursor.close()

    fig, ax = plt.subplots(figsize=(12,6.5)) 
    ax.plot(hour, temp)
    ax.set_xlim(0, 24)
    ax.set_ylim((min(temp)-2), (max(temp)+2))
    ax.xaxis.set_major_locator(MultipleLocator(1)) 
    ax.yaxis.set_major_locator(MultipleLocator(1))
    ax.set_title("Temperature Tracker")
    ax.set_xlabel("Time of Day")
    ax.set_ylabel("Temperature")
    # Save it to a temporary buffer.
    buf = BytesIO()
    plt.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    plt.close()
    buf.close()
    return data