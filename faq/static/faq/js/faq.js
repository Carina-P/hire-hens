/**
 * To manage the accordion actions in FAQ page.
 **/
let acc = document.getElementsByClassName("accordion");

for (let i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function () {
        this.classList.toggle("active");
        let panel = this.nextElementSibling;
        if (panel.style.maxHeight) {
            panel.style.maxHeight = null;
        } else {
            panel.style.maxHeight = panel.scrollHeight + "px";
        }
    });
}

/** 
 * Manage Modal
 **/
function openRemoveModalFaq(faqId) {
    if (faqId === undefined || faqId === null) {
        console.log(
            "Error in function openRemovefaq, questionId undefined");
        return;
    }

    $('#hidden_faq').html(`<input type="hidden" name="faq_id" value="${faqId}">`)
    $('#modal_remove_faq').modal('show');
}