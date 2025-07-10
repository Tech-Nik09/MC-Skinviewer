import get_api_request as api
import streamlit as st

st.title("MC Skinviewer by :blue[Niklas Maroldt]", anchor=None, help=None, width="stretch")

playername = st.text_input("label", value="Redstone31v", max_chars=16, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder="Search minecraft gamertag:", disabled=False, label_visibility="hidden", icon=None, width="stretch")
if playername == "":
    playername = "Redstone31v"
    print("[INFO] No playername specified. Set playername to default.")
uuid = api.get_uuid(playername)


st.divider()
st.markdown(f"UUID of player {playername}: *{uuid}*")
st.divider()


image_shadow = st.toggle("Cast shadow", value=True, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible", width="content")
image_cape = st.toggle("Cape visibility", value=True, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible", width="content")
image_helmet = st.toggle("Head: second layer", value=True, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible", width="content")
image_overlay = st.toggle("Body: second layer", value=True, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible", width="content")

image_yaw = st.slider("Skin rotation", min_value=0, max_value=360, value=0, step=10, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible", width="stretch")


image_url = api.get_image_url(uuid, yaw=image_yaw, shadow=image_shadow, cape=image_cape, helmet=image_helmet, overlay=image_overlay)



st.image(image_url, caption = f"Current skin of {playername}")

skin_binary_data = api.get_skin_data(uuid)
st.download_button("Download Skin", skin_binary_data, file_name=f"{playername}_skin.png", mime="image/png", key=None, help=None, on_click="rerun", args=None, kwargs=None, type="primary", icon=None, disabled=False, use_container_width=True)

