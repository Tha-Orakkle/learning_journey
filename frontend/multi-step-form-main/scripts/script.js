let currentStep = 1;
emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
phoneRegex = /^(\+\d{1, 4})?\d{10}$/;

function showStep(stepNum) {
    const steps = document.querySelectorAll('.steps')
    steps.forEach((step) => {
        step.style.display = 'none';
    });

    const pageNums = document.querySelectorAll('.num-page');
    pageNums.forEach((num) => {
        num.classList.remove('num-page');
    })

    const currentStepElement = document.getElementById(`step${stepNum}`);

    const numPage = document.getElementById(`num${stepNum}`)
    if (currentStepElement) {
        if (numPage) {
            numPage.classList.add('num-page')
        }
        currentStepElement.style.display = 'block';
    }

}

function nextStep() {
    if (currentStep < 4) {
        currentStep++;
        showStep(currentStep);
    }
}

function prevStep() {
    if (currentStep > 1) {
        currentStep--;
        showStep(currentStep);
    }
}

function confirm() {
    const steps = document.querySelectorAll('.steps');
    steps.forEach((step) => {
        step.style.display = 'none';
    });
    const currentStepElement = document.getElementById(`step5`);

    if (currentStepElement) {
        currentStepElement.style.display = 'block';
    }
}


showStep(currentStep);


const firstNextBtn = document.querySelector('.bottom-nav-first button');
firstNextBtn.addEventListener('click', function () {

    var nodeRemove = document.querySelectorAll('.req')
    nodeRemove.forEach(function (node) {
        node.parentNode.removeChild(node)
    })
    var req = document.createElement('span');
    req.classList.add('req');
    

    const name = document.getElementById('name')
    const email = document.getElementById('email')
    const telephone = document.getElementById('telephone')

    if (name.value.trim() === '') {
        var pNode = document.getElementById('name-input')
        req.textContent = 'this field is required'
        pNode.appendChild(req)
    } else if (email.value.trim() === '' || !(emailRegex.test(email.value.trim()))) {
        var pNode = document.getElementById('email-input')
        req.textContent = 'Invalid Email';
        pNode.appendChild(req)
    } else if (telephone.value.trim() === '' || !(phoneRegex.test(telephone.value.trim()))) {
        var pNode = document.getElementById('telephone-input');
        req.textContent = 'Invalid telephone'
        pNode.appendChild(req)
    } else {
        var formName = name.value.trim();
        var formEmail = email.value.trim();
        var formPhone = telephone.value.trim();

        nextStep();
    }

});

