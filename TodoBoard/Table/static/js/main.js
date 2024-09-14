 // todoTable 또는 todoText 클릭 시 모달 띄우기
 document.querySelectorAll('.table-box2').forEach(function(tableBox2) {
    var todoTable = tableBox2.querySelector('input[id^="todoTable"]');
    var todoText = tableBox2.querySelector('input[id^="todoText"]');

    todoTable.onclick = function() {
        openModal(tableBox2);
    };
    todoText.onclick = function() {
        openModal(tableBox2);
    };
});

    // 모달 관련 자바스크립트
    var modal = document.getElementById("myModal");
    var closeModal = document.getElementsByClassName("close")[0];

    // table-box 클릭 시 모달 띄우기
    document.querySelectorAll(".table-box2").forEach(function(tableBox2) {
        tableBox2.onclick = function() {
            var todoContent = this.getAttribute("data-todo");
            var todoText = this.getAttribute("data-text");
            var todoId = this.getAttribute("data-id");

            // 모달 내용 업데이트
            document.getElementById("editTodoTable").value = todoContent;
            document.getElementById("editTodoText").value = todoText;
            document.getElementById("editTodoId").value = todoId;

            // 모달 보이기
            modal.style.display = "block";
        };
    });

    // 모달 닫기 버튼
    closeModal.onclick = function() {
        modal.style.display = "none";
    };

    // 모달 외부 클릭 시 닫기
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    };
