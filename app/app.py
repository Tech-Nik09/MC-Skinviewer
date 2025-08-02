import api_client
import streamlit as st

st.set_page_config(page_title="NM-Skinviewer", page_icon=":art:", layout="wide", initial_sidebar_state=None, menu_items=None)

st.markdown(
        f"""
        <p style='text-align: center; font-family: "Arial"; font-size: 50px; font-weight: bold;'>MC Skinviewer by Niklas Maroldt</p>
        """,
        unsafe_allow_html=True
)


user_input = st.text_input("label", value="", max_chars=16, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder="Search minecraft gamertag:", disabled=False, label_visibility="hidden", icon=None, width="stretch")
player_info = api_client.get_player_information(user_input)
if "id" in player_info:
    uuid = player_info["id"]
    playername = player_info["name"]
elif user_input == "":
    uuid = "069a79f444e94726a5befca90e38aaf5"
    playername = "Notch"
else:
    st.error("Please enter a valid username!")
    uuid = "069a79f444e94726a5befca90e38aaf5"
    playername = "Notch"


col1, col2 = st.columns([0.3, 0.7],gap="small", vertical_alignment="top", border=True)

with col1:
    st.markdown(
        f"""
        <p style='text-align: center; font-family: "Arial"; font-size: 40px; font-weight: bold;'>Properties</p>
        <hr>
        """,
        unsafe_allow_html=True
    )
    image_shadow = st.toggle("Cast shadow", value=True, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible", width="content")
    image_cape = st.toggle("Cape visibility", value=True, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible", width="content")
    image_helmet = st.toggle("Head: second layer", value=True, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible", width="content")
    image_overlay = st.toggle("Body: second layer", value=True, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible", width="content")
    image_yaw = st.slider("Skin rotation", min_value=0, max_value=360, value=0, step=30, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible", width="stretch")

with col2:
    image_url = api_client.get_image_url(uuid, yaw=image_yaw, shadow=image_shadow, cape=image_cape, helmet=image_helmet, overlay=image_overlay)
    st.markdown(
        f"""
        <div style='text-align: center;'>
            <p style='font-family: "Arial"; font-size: 40px; font-weight: bold;'>{playername}</p>
            <hr>
            <img src='{image_url}'>
        </div>
        """,
        unsafe_allow_html=True
    )    
    st.badge("Rendering powered by VZGE (SurgePlay Visage)", icon=":material/electric_bolt:", color="green", width="content")


with st.container(height=None, border=True, key=None):
    st.markdown(
        f"""
        <p style='text-align: center; font-family: "Arial"; font-size: 40px; font-weight: bold;'>UUID</p>
        <p style='text-align: center; font-family: "Arial"; font-size: 30px; font-weight: bold; font-style: italic;'>{uuid}</p>
        """,
        unsafe_allow_html=True
    )


with st.container(height=None, border=True, key=None):
    st.markdown(
        f"""
        <p style='text-align: center; font-family: "Arial"; font-size: 40px; font-weight: bold;'>Downloads</p>
        """,
        unsafe_allow_html=True
    )
    skin_binary_data = api_client.get_skin_data(uuid)
    st.download_button(f"Download skin of {playername}", skin_binary_data, file_name=f"{playername}_skin.png", mime="image/png", key=None, help=None, on_click="ignore", args=None, kwargs=None, type="primary", icon=None, disabled=False, use_container_width=True)
    preview_binary_data = api_client.get_preview_image(image_url)
    st.download_button(f"Download preview image", preview_binary_data, file_name=f"{playername}_preview.png", mime="image/png", key=None, help=None, on_click="ignore", args=None, kwargs=None, type="primary", icon=None, disabled=False, use_container_width=True)
