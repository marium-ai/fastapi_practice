from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 1. Yeh aapka mobile phone hai, jisme abhi aapka naam aur bio save hai
my_profile = {
    "name": "Ayesha",
    "bio": "Available"
}

# 2. Yeh batane ke liye ke user naya bio kya bhej raha hai
class UpdateBio(BaseModel):
    new_bio: str


# --- AB DHEKHEIN PUT API KA ASLI AUR SABSE SIMPLE CODE ---
@app.put("/update-profile")
def change_my_bio(profile_data: UpdateBio):
    
   
    my_profile["bio"] = profile_data.new_bio
    
    return {
        "message": "Profile Updated Successfully!",
        "current_profile": my_profile
    }