import get_api_request as api
import streamlit as st

st.set_page_config(page_title="NM-Skinviewer", page_icon=":art:", layout="wide", initial_sidebar_state=None, menu_items=None)

st.markdown(
        f"""
        <p style='text-align: center; font-family: "Arial"; font-size: 50px; font-weight: bold;'>MC Skinviewer by Niklas Maroldt</p>
        """,
        unsafe_allow_html=True
)

playername = st.text_input("label", value="notch", max_chars=16, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder="Search minecraft gamertag:", disabled=False, label_visibility="hidden", icon=None, width="stretch")
if playername == "":
    playername = "notch"
    print("[INFO] No playername specified. Set playername to default.")
uuid = api.get_uuid(playername)


with st.container(height=None, border=True, key=None):
    st.markdown(
        f"""
        <p style='text-align: center; font-family: "Arial"; font-size: 40px; font-weight: bold;'>UUID</p>
        <p style='text-align: center; font-family: "Arial"; font-size: 30px; font-weight: bold; font-style: italic;'>{uuid}</p>
        """,
        unsafe_allow_html=True
    )


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
    image_url = api.get_image_url(uuid, yaw=image_yaw, shadow=image_shadow, cape=image_cape, helmet=image_helmet, overlay=image_overlay)
    st.markdown(
        f"""
        <div style='text-align: center;'>
            <p style='font-family: "Arial"; font-size: 40px; font-weight: bold;'>Player</p>
            <hr>
            <img src='{image_url}'>
        </div>
        """,
        unsafe_allow_html=True
    )    


with st.container(height=None, border=True, key=None):
    st.markdown(
        f"""
        <p style='text-align: center; font-family: "Arial"; font-size: 40px; font-weight: bold;'>Download</p>
        """,
        unsafe_allow_html=True
    )
    skin_binary_data = api.get_skin_data(uuid)
    st.download_button(f"Download current skin of {playername}", skin_binary_data, file_name=f"{playername}_skin.png", mime="image/png", key=None, help=None, on_click="rerun", args=None, kwargs=None, type="primary", icon=None, disabled=False, use_container_width=True)
