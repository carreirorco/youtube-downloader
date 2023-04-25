import streamlit as st
from pytube import YouTube

st.title("Youtube Downloader")
st.subheader("Insira a URL do vídeo: ")
url = st.text_input("URL: ")

if url != "":
    yt = YouTube(url)
    st.image(yt.thumbnail_url, width=300)
    st.subheader("""
    {}
    # Lenght: {} seconds
    # Rating: {}
    """.format(yt.title, yt.length, yt.rating))

    video = yt.streams
    if len.video > 0:
        downloaded, download_video = False, False
        download_video = st.button("Baixar vídeo")

        if yt.streams.filter(only_audio=True):
            download_audio = st.button("Baixar somente o audio")
        if download_video:
            video.get_lowest_resolution().download()
            downloaded = True
        if download_audio:
            video.download(only_audio=True).first().download()
            downloaded = True
        if downloaded:
            st.subheader("Download Concluído!")
    else:
        st.subheader("Não foi possível baixar o vídeo")