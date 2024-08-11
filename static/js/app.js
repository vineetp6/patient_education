document.addEventListener('DOMContentLoaded', function () {
    var searchLinks = document.querySelectorAll('.search-link');
    
    searchLinks.forEach(function (link) {
        link.addEventListener('click', function (event) {
            event.preventDefault();
            var query = this.getAttribute('data-query');
            var form = document.getElementById('search-form');
            var input = form.querySelector('input[name="query"]');
            input.value = query;
            form.submit();
        });
    });
});

function calculateBMI() {
    var height = document.getElementById('height').value;
    var weight = document.getElementById('weight').value;

    if (height > 0 && weight > 0) {
        var bmi = (weight / ((height / 100) * (height / 100))).toFixed(2);
        document.getElementById('bmi-result').innerText = 'Your BMI is ' + bmi;
    } else {
        document.getElementById('bmi-result').innerText = 'Please enter valid height and weight';
    }
}

function calculateCalories() {
    var age = document.getElementById('age').value;
    var gender = document.getElementById('gender').value;
    var activityLevel = document.getElementById('activity-level').value;
    
    if (age > 0) {
        var bmr;
        if (gender === 'male') {
            bmr = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age);
        } else {
            bmr = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age);
        }
        
        var activityMultiplier;
        switch (activityLevel) {
            case 'sedentary':
                activityMultiplier = 1.2;
                break;
            case 'light':
                activityMultiplier = 1.375;
                break;
            case 'moderate':
                activityMultiplier = 1.55;
                break;
            case 'active':
                activityMultiplier = 1.725;
                break;
        }
        
        var dailyCalories = (bmr * activityMultiplier).toFixed(2);
        document.getElementById('calories-result').innerText = 'Your daily calorie needs are ' + dailyCalories + ' calories';
    } else {
        document.getElementById('calories-result').innerText = 'Please enter valid age';
    }
}
