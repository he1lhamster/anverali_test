
function createOrderClick() {
    console.log('start')

    const customerId = document.getElementById('customer_id').value;
    const title = document.getElementById('title').value;
    const description = document.getElementById('description').value;
    const orderCategory = document.getElementById('order_category').value;

    fetch(`/api/orders/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({
            customer: customerId,
            title: title,
            description: description,
            order_category: orderCategory
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Возникла ошибка при создании заказа.');
        }
        alert('Заказ успешно создан.');
         window.location.reload();
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Возникла ошибка при создании заказа.');
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function updateOrder(event) {

    const orderId = event.target.dataset.orderId;
    const performerId = event.target.dataset.performerId;
    const statusId = event.target.dataset.statusId;
    let rateId = null
    const ratingInput = this.previousElementSibling;

    if (ratingInput && ratingInput.tagName === "INPUT" && ratingInput.value) {
        rateId = ratingInput.value;
    }

    const orderUpdateData = {
    ...(performerId ? { performer: parseInt(performerId) } : {}),
    ...(statusId ? { status: parseInt(statusId) } : {}),
    ...(rateId ? { rate: parseInt(rateId) } : {})
    };
    if (Object.keys(orderUpdateData).length !== 0) {
        console.log(orderUpdateData)
        fetch(`/api/orders/${orderId}/`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify(orderUpdateData)
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Возникла ошибка при обновлении заказа.');
                }
                alert('Заказ успешно обновлен.');
                window.location.reload()
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Возникла ошибка при обновлении заказа.');
            });
    }

}

const buttons = document.getElementsByClassName('updateOrderBtn');
        for (let i = 0; i < buttons.length; i++) {
            buttons[i].addEventListener('click', updateOrder);
        }
