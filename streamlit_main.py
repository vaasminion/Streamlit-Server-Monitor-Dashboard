import streamlit as st
import pandas
import datetime
from ping import ping_check
from config import getServers

def is_server_reachable(server_address):
    return ping_check(server_address,1)
def statusColor(value):
    if value == 'REACHABLE':
        color = "background-color: green;font-weight: bold;"
    elif value == 'UNREACHABLE':
        color = "background-color: red;font-weight: bold;"
    else:
        color = "font-weight: bold"
    return color
def get_server_status(server_list):
    """Queries servers and returns their reachability status."""
    server_data = []
    for server in server_list:
        name = server['NAME']
        address = server['HOST']
        reachable = is_server_reachable(address)
        status =  'REACHABLE' if reachable else 'UNREACHABLE'
        server_data.append((name,status))
    print(server_data)
    df = pandas.DataFrame(server_data,columns = ['HOSTNAME-IP','STATUS'])
    #df = df.set_index(df.columns[0])
    df = df.style.applymap(statusColor, subset=['HOSTNAME-IP','STATUS'])

    return df

st.set_page_config(page_title="Server Monitoring Dashboard", page_icon=":computer:")

# Get server list from user input or configuration file
server_list = getServers()['serverList'] # Replace with your server list or add input mechanisms
if not server_list:
    st.header('SERVER HEALTH CHECK REPORT')
    st.error("Please provide a list of servers to monitor.")
else:

    st.header('SERVER HEALTH CHECK REPORT')
    ist_offset = datetime.timedelta(hours=5, minutes=30)
    currenttime = datetime.datetime.now() + ist_offset
    st.header(f'LAST UPDATED ON {currenttime.strftime("%m/%d/%Y, %H:%M:%S")} IST')
    server_data = get_server_status(server_list)
    st.table(server_data)
    # # Refresh button for manual updates
    if st.button("Refresh"):
        st.empty()
