import streamlit as st
import all_oils
from ai import prompt

st.session_state["initialized"] = False
def init_app():
    if st.session_state["initialized"] == False:
        st.session_state["initialized"] = True
        prompt.start_models()

# Stage 1: Welcome and pick oils
def welcome_and_pick_oils():
    init_app()
    st.title("Welcome to Your Personalized Salt Scrub App!")
    st.subheader("Step 1: Choose Your Oils")

    oils = [o.name.lower() for o in all_oils.get_all_oils()]

    # User selects oils
    oils = st.multiselect(
        "Pick your favorite oils:",
        options=oils
    )
    # Proceed button
    if st.button("Next"):
        st.session_state["stage"] = "instructions"
        st.session_state["oils"] = oils
        st.rerun()


# Stage 2: Instruction for wanted scent
def instruction_for_scent():
    st.title("Step 2: Customize Your Scent")
    st.write(f"You've selected: {', '.join(st.session_state['oils']) or 'No oils selected'}")

    # User provides instructions for scent
    scent_instruction = st.text_area(
        "Describe the scent you'd like to create (e.g., calming, invigorating):"
    )
    placeholder = st.empty()
    # Proceed button

    with placeholder:
        if st.button("Finished"):
            st.session_state["stage"] = "salt_scrub"
            st.session_state["scent_instruction"] = scent_instruction
            placeholder.empty()
            st.rerun()


# Stage 3: Instructions for creating the salt scrub
def salt_scrub_instructions():
    import ai.prompt

    st.title("Step 3: Your Custom Fragrance")
    st.write("")
    available_oils = st.session_state['oils']
    instructions = st.session_state['scent_instruction']
    placeholder = st.empty()
    with placeholder.container():
        st.subheader("Crafting Your Perfect Scent...")
        st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExYTVoMjV1aDZtY2Uwd3dqb3JudG02Yzl3bzN2Y2phOWZnd2s0Z3ZjbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l0Iyb2pEevoDThkFW/giphy.webp", width=150)
        message = ai.prompt.to_prompt(available_oils, instructions)
        reciepe, proportions = ai.prompt.run_ollama_model(message)
        placeholder.empty()
    st.write(reciepe)
    st.write(proportions)
    st.title("Step 4:Salt Scrub Recipe")
    st.write("**Ingredients:**")
    st.write("- 1 cup of salt (e.g., sea salt or Himalayan salt)")
    st.write("- 1/4 cup of selected oils (any refined oil can be used - almond, grape-seed, avocado etc..)")
    for oil, per in proportions.items():
        st.write(f"- Add {int(per*30)} drops of {oil}")
    st.write("**Instructions:**")
    st.write("1. Combine the salt and oils in a bowl.")
    st.write("2. Mix thoroughly until well combined.")
    st.write("3. Store in an airtight container and enjoy!")

    # Restart button
    if st.button("Restart"):
        st.session_state["stage"] = "welcome"
        st.rerun()


# Initialize session state
if "stage" not in st.session_state:
    st.session_state["stage"] = "welcome"
    st.session_state["process_complete"] = False
# Route through stages
if st.session_state["stage"] == "welcome":
    welcome_and_pick_oils()
elif st.session_state["stage"] == "instructions":
    instruction_for_scent()
elif st.session_state["stage"] == "salt_scrub":
    salt_scrub_instructions()
