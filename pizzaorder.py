import streamlit as st

# -- Page Header --
st.header("Interactive pizza calcuator")
st.markdown("Customize your order below")
st.divider()

#-- user input --
st.subheader("Configure your pizza")

#-- size selection --
pizza_size = st.selecbox("Choose Pizz Size: ", ["Small", "Medium", "Large"])

# -- crust selection --
crust_type = st.selectbox("Choose Crust Type: ", ["Thin", "Thick", "Stuffed"])

# -- topping selection --
st.markdown("Add extra toppings ₹40 each")
add_cheese = st.checkbox("Extra Mozzarella Cheese")
add_mushroon = st.checkbox("Extra Mushroom")
add_chicken = st.checkbox("Extra Chicken")
add_paneer = st.checkbox("Extra Paneer")

# Voucher System
coupon_code = st.text_input("Have a Promo Code? Enter it here:").strip().upper()

st.divider()

base_price = 0
crust_fee = 0
topping_count = 0
discount = 0

if pizza_size == "Small":
    base_price = 399
elif pizza_size == "Medium":
    base_price = 599
else:
    base_price = 799


if crust_type == "Stuffed Crust (+₹150)":
    crust_fee = 150


if add_cheese:
    topping_count = topping_count + 1

if add_mushroon:
    topping_count = topping_count + 1

if add_chicken:
    topping_count = topping_count + 1

if add_paneer:
    topping_count = topping_count + 1


topping_total_cost = topping_count * 40
subtotal = base_price + crust_fee + topping_total_cost

if coupon_code == "PIZZA50":
    discount = 50  # Flat ₹50 off

final_total = subtotal - discount 

st.subheader("🛍️ Your Final Bill Summary")


col1, col2 = st.columns(2)

with col1:
    st.markdown(f"*Selected Item:* {pizza_size} Pizza ({crust_type})")
    st.markdown(f"*Total Extra Toppings Added:* {topping_count}")
    
  
with col2:
    st.metric(label="Subtotal", value=f"₹{subtotal}")
    if discount > 0:
        st.metric(label="Discount Applied", value=f"-₹{discount}", delta="Promo Saved!")
    st.metric(label="Final Total Amount Due", value=f"₹{final_total}")
