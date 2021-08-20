// function postComment(book_id) {
//   let content = $("#comment-content").val();
//   let rating = $("#star").val();

//   $.ajax({
//     url: "/create-comment",
//     type: "post",
//     data: {
//       book_id: book_id,
//       content: content,
//       rating: rating,
//     },
//     success: function (res) {
//       let result = res["result"];
//       if (result == "success") {
//         window.location.reload();
//       } else {
//         alert("다시 등록해 주세요.");
//       }
//     },
//   });
// }

function getDetail(book_id) {
  $.ajax({
    url: "/detail",
    type: "get",
    datatype: "json",
    data: {
      book_id: book_id,
    },
  });
}

function postComment(book_id) {
  let content = ducoment.querySelector("#comment-content").value;
  let ratings = document.getElementsByName("rating");
  let rating = 0;
  ratings.forEach((node) => {
    if (node.checked) {
      rating += 1;
      return;
    }
  });

  $.ajax({
    url: "/create-comment",
    type: "post",
    datatype: "json",
    data: {
      book_id: Number(book_id),
      content: content,
      rating: Number(rating),
    },
    success: function (res) {
      let result = res["result"];
      if (result == "success") {
        window.location.reload();
      } else {
        alert("다시 입력하세요.");
      }
    },
  });
}

const ratingResult = () => {
  let ratingData = document
    .querySelector(".rating-result")
    .getAttribute("data");
  let star = document.querySelectorAll("#star");
  for (let i = 0; i < Number(ratingData); i++) {
    star[i].classList.add("checked");
  }
};
