const form = document.getElementById("product-form");
const productList = document.getElementById("product-list");
const message = document.getElementById("message");


async function loadProducts() {
    const response = await fetch("/products");
    const products = await response.json();

    productList.innerHTML = "";

    for (const product of products) {
        const item = document.createElement("li");

        item.textContent =
            `${product.name} — Quantity: ${product.current_quantity}, ` +
            `Minimum: ${product.minimum_stock_level}`;

        productList.appendChild(item);
    }
}


form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const product = {
        name: document.getElementById("name").value,
        current_quantity: Number(
            document.getElementById("current-quantity").value
        ),
        minimum_stock_level: Number(
            document.getElementById("minimum-stock-level").value
        ),
    };

    const response = await fetch("/products", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(product),
    });

    if (!response.ok) {
        message.textContent = "Could not add product.";
        return;
    }

    message.textContent = "Product added successfully.";

    form.reset();

    document.getElementById("current-quantity").value = 0;
    document.getElementById("minimum-stock-level").value = 0;

    await loadProducts();
});


loadProducts();