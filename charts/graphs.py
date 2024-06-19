import plotly.express as px
import plotly.graph_objects as go
import base64
import pandas as pd
import plotly.io as pio

def plot_graph(df):
    try:
        print("DF completed")
        # fig = px.line(df, x="TimeStamp", y="Value", color="Name")
        fig = px.line(df, x="TimeStamp", y="Value", color = "Name", markers=True) 
        #fig.update_yaxes(range(0,100))   
        print("Fig completed")                                                                              
        # for i in range (1,20):
        #     df1 = df.head(10000*i)
        #     fig = px.line(df1, x="TimeStamp", y="Value", color = "Name", markers=True)
        #     browser.setHtml(fig.to_html(include_plotlyjs='cdn')) 
        #     time.sleep(5000)
        print("HTML completed")
        return fig
    except Exception as e:
        print(f"Error: {e}")

def report_graph(df):
    try:
        print("DF completed")
        fig = px.line(df, x="TimeStamp", y="Value", color="Name", markers=True)
        graph_image_path = "graph.png"
        pio.write_image(fig, graph_image_path, format='png')
        with open(graph_image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            encoded_image = f"data:image/png;base64,{encoded_string}"
        return encoded_image
    except Exception as e:
        print(f"Error: {e}")

def show_bar(engineConRead):
    try:
        sql = """
                SELECT TimeStamp, Value
                FROM plc_data
                WHERE TimeStamp >= DATEADD(WEEK, -1, GETDATE())
                """
        df_bargh = pd.read_sql_query(sql, engineConRead)
        df = df_bargh

        df['TimeStamp'] = pd.to_datetime(df['TimeStamp'], errors='coerce', infer_datetime_format=True)

        # Set the TimeStamp column as the index
        df.set_index('TimeStamp', inplace=True)

        # Resample by day and count the number of entries for each day
        daily_counts = df.resample('D').size()

        # Convert the resampled data into a DataFrame for plotting
        daily_counts_df = daily_counts.reset_index(name='count')

        # Create the bar graph using Plotly
        fig = px.bar(daily_counts_df, x='TimeStamp', y='count', title='Count of Data Points per Day')

        return fig

    except Exception as e:
        print(f"Error: {e}")

def show_speed(Total_seconds):
        try:
        
            # Convert Total_seconds to float or int, depending on your data type
            value = float(Total_seconds)  # Assuming Total_seconds is a string representation of a number
            
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=value,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "Speed in sec of Data Fetching from PLC"},
                gauge = {
            'axis': {'range': [None, 10], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 2.5], 'color': 'cyan'},
                {'range': [2.5, 5], 'color': 'royalblue'}],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 7}}))
            fig.update_layout(paper_bgcolor = "#ECF1F7", font = {'color': "#171725", 'family': "Black"})
            return fig
         

        except Exception as e:
            print(f"Error: {e}")    