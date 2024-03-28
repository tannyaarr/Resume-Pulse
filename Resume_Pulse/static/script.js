function selectCareerPath() {
    var careerPath = document.getElementById("careerPath").value;
    
    fetch('/select_career_path', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: 'career_path=' + careerPath
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === 'Career path selected successfully') {
            document.getElementById("careerPathSelection").style.display = "none";
            document.getElementById("groupsList").style.display = "block";
            fetchGroups();
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function fetchGroups() {
    fetch('/get_groups')
    .then(response => response.json())
    .then(data => {
        if (data.groups) {
            var groupsList = document.getElementById("groups");
            groupsList.innerHTML = '';
            data.groups.forEach(group => {
                var listItem = document.createElement("li");
                listItem.textContent = group.name + ': ' + group.description;
                groupsList.appendChild(listItem);
            });
        } else {
            console.error('Error: ', data.error);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
