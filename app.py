import streamlit as st

st.title("Tell Ro and Grampy Your Name")
st.write("Paste text here for diagnosis")

fam_dict = {"Jon": "brilliant", "Will": "foolish wood-maker", "Cath": "kitchen perfectionista", "Em": "too many outbuildings"}

text = st.text_area ("Your text", height =200)

if text:
      
	    
	st.subheader("How Much Do You Love Ro and Grampy")
	st.write(f"**{text}** loves Ro and Grampy very much")
	new_text = ""
	for letter in text:
		new_text += letter.upper()
	print (f"""Here's your name in UPPER CASE: {new_text}""")

print (fam_dict[text])


	

