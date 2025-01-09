{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9079bd5c-7013-4716-a48f-754fd4f05b26",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Transcription téléchargée et enregistrée dans 'transcription.txt'.\n"
     ]
    }
   ],
   "source": [
    "from youtube_transcript_api import YouTubeTranscriptApi\n",
    "from youtube_transcript_api.formatters import TextFormatter\n",
    "\n",
    "# ID de la vidéo YouTube (extrait de l'URL : https://www.youtube.com/watch?v=VIDEO_ID)\n",
    "video_id = \"dxkk56oLpTk\"\n",
    "\n",
    "try:\n",
    "    # Récupération de la transcription en français\n",
    "    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['fr'])\n",
    "\n",
    "    # Formater la transcription en texte simple\n",
    "    formatter = TextFormatter()\n",
    "    transcript_text = formatter.format_transcript(transcript)\n",
    "\n",
    "    # Sauvegarder dans un fichier texte\n",
    "    with open(\"transcription.txt\", \"w\", encoding=\"utf-8\") as file:\n",
    "        file.write(transcript_text)\n",
    "\n",
    "    print(\"Transcription téléchargée et enregistrée dans 'transcription.txt'.\")\n",
    "\n",
    "except Exception as e:\n",
    "    print(f\"Erreur : {e}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0d17500d-7887-4a64-a744-6441051d4d43",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
