$(document).ready(function (event) {
	var dart_score = new DartScore();

	$('div.point_calculator button.point_input_btn.point_number').on('click', function (event) {
		dart_score.scoreInput($(event.target).attr('data-value'));
	});
	$('div.point_calculator button.point_input_btn.point_clear').on('click', function (event) {
		dart_score.clearScore();
	});
	$('button.point_ok').on('click', function (event) {
		dart_score.okScore();
	});
});

function DartScore () {
	var score_window_id = 'score_window';
	var point_input_id = 'points_input';
	var score = '0';
	this.scoreInput = function (number) {
		if (score.length >= 3 || parseInt(score) == 0) {
			score = number;
		} else {
			score = score + number;
		}
		$('#' + score_window_id).html(score);
	}
	this.clearScore = function () {
		score = '0';
		$('#' + score_window_id).html(score);
	};
	this.okScore = function () {
		$('#' + point_input_id).val(parseInt(score));
		$('#' + point_input_id).text(parseInt(score));
	};
}