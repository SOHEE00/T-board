function toggleMemoBox(button) {
    // 클릭된 버튼의 부모 요소인 timebox를 찾습니다.
    var ckDiv = button.closest(".timebox");

    // hidden-content 요소를 찾습니다.
    var hiddenContent = ckDiv.querySelector('.hidden-content');

    // hidden-content의 표시 상태를 토글합니다.
    if (hiddenContent.style.display === 'block') {
        hiddenContent.style.display = 'none';
    } else {
        hiddenContent.style.display = 'block';
    }
}

function toggleDoneBox(button) {
    var ckDiv = button.closest(".timebox2");

    // hidden-content 요소를 찾습니다.
    var hiddenContent = ckDiv.querySelector('.hidden-content');

    // hidden-content의 표시 상태를 토글합니다.
    if (hiddenContent.style.display === 'block') {
        hiddenContent.style.display = 'none';
    } else {
        hiddenContent.style.display = 'block';
    }
}