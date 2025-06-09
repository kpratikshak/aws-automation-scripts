qa_visual_response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            {"role"": ""system"", "content": ""You are a helpful assistant."},
             {"role"": ""user","content":[
                 "These are the frames from the video",
                 *map(lambda x: {"type": "image_url", "image_url",
                 "image_url":f"data:image/jpg;base64,{x}"}, "detail": "low"}},
              base64Frames)
             ],
        }
    ],
temperature=0,
)
print(response.choices[0].message.content)

with open(audio_path,"rb") as audio_file:
    audio_content= base64.b64encode(audio_file.read()).decode("utf-8")
    
response =client.chat.completions.create(
    model="gpt-4o-audio-preview",
    modalities=["text"],
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "These are the frames from the video",
            "audio": audio_content
        },
    ]
    }
temperature=0,
)

transcription = response.choices[0].message.content
print(transcription)

response  = client.chat.completions.create(
    model=MODEL,
    modalities=["text"],
    messages=[
        {"role":"system","content":"You are generating a transcript }
    ]
    
    def upload_file(file_path:str,vector_store_id:str):
    file_name = os.path.basename(file_path)
    try:
        file_response = client.files.create(file=open(file_path,"rb"),purpose="assistants")
        attach_response = client.vector_stores.files.create(
            vector_store_id=vector_store_id,
            file_id=file_response.id
        )
    return {"file":file_name,"status":"success"}
  except Exception as e:
      print(f"Error with {file_name}:{str(e)}")
      return {"file":file_name,"status":"failed"}
      
    def create_vector_store(store_name:str)-> dict:
        try:
            vector_store= client.vector_stores.create(name=store_name)
            details={
                "id":vector_store.id,
                "name":vector_store.name,
                "created_at":vector_store.created_at,
                "file_count":vector_store.file_counts.completed
            }
            print("vector store created:",details)
            return details
    except Exception as e:
            print(f"Error creating vector store:{str(e)}")
            return {}
vector_store_id = create_vector_store("ACME Shop product knowledge Base")
upload_file["voice_agents_knowledge/acme_product_catalogue.pdf",vector_store_id["id"])
 
knowledge_agent = Agent(
    name=
)
 
knowledge_agent = Agent(
    name=
)
 
knowledge_agent = Agent(
    name=
)
)knowledge_agent = Agent(
    name=
)