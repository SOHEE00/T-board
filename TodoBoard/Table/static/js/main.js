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

// table-box2, todoTable, todoText 클릭 시 모달 띄우기
document.querySelectorAll(".table-box2, #todoTable, #todoText").forEach(function(element) {
    element.onclick = function() {
        var tableBox2 = this.closest('.table-box2');  // .table-box2를 찾아 해당 데이터 속성 참조

        var todoContent = tableBox2.querySelector('#todoTable').value;  // 제목 값
        var todoText = tableBox2.querySelector('#todoText').value;  // 텍스트 값
        var todoId = tableBox2.querySelector('#todoNum').value;  // todo id 값

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
    //별 버튼
    $('.btn-star').on('click', function(event) {
        event.preventDefault();  // 기본 form 제출 방지
    
        let button = $(this);
        let form = button.closest('form');
        let todoId = form.data('todo-id');  // form 태그의 data-todo-id 속성을 가져옴
        let csrfToken = form.find('input[name="csrfmiddlewaretoken"]').val();  // CSRF 토큰 가져오기
    
        // 콘솔로 값 출력해서 디버깅
        console.log("Todo ID: " + todoId);
        console.log("CSRF Token: " + csrfToken);
    
        $.ajax({
            url: './markAsStar/',  // 서버로 POST 요청 보낼 URL
            type: 'POST',
            data: {
                todo_id: todoId,
                csrfmiddlewaretoken: csrfToken  // CSRF 토큰 추가
            },
            success: function(response) {
                console.log('서버 응답 성공:', response);
    
                // 서버 응답이 성공적일 경우, 버튼의 색깔 및 텍스트를 변경
                if (button.text() === '☆') {
                    button.text('★');
                    button.css('color', 'orange');
                } else {
                    button.text('☆');
                    button.css('color', 'black');
                }
            },
            error: function(xhr, status, error) {
                console.error('별표 처리 실패:', error);
                console.error('응답 상태:', xhr.status);
            }
        });
    });

document.getElementById('todoImage').addEventListener('change', function(event) {
        var file = event.target.files[0];
        var reader = new FileReader();
    
        reader.onload = function(e) {
            var imagePreview = document.getElementById('imagePreview');
            imagePreview.src = e.target.result;
            imagePreview.style.display = 'block'; // 이미지 미리보기 보이도록 설정

            // 파일 입력 필드를 숨깁니다.
            event.target.style.display = 'none';
        };
    
        if (file) {
            reader.readAsDataURL(file);
        }
});