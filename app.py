import streamlit as st

st.title("Tell Ro and Grampy Your Name")
#st.write("Paste text here for diagnosis")

text = st.text_area ("Your text", height =200)

fam_dict = {"Jon": "brilliant", "Will": "foolish wood-maker", "Cath": "kitchen perfectionista", "Em": "too many outbuildings", "Dave": "only lifts 5kg dumbbells"}
	
if st.button("Diagnosis!"):
	if text in fam_dict:
          
		st.subheader("How Much Do You Love Ro and Grampy")
		st.write(f"**{text}** loves Ro and Grampy very much")
		new_text = ""
	
		for letter in text:
			new_text += letter.upper()
		st.write (f"""Here's your name in UPPER CASE: {new_text}""")
		st.subheader("What do they think of you?")
		st.write (fam_dict[text])

	else:

		st.write("Don't know you")
	

