import bot_logic.command_functions as comFunc

commandHandler = {
  "inspiro": comFunc.get_inspiro_pic,
  "number": comFunc.get_random_number,
  "test": comFunc.get_test,
  "jn": comFunc.get_yes_or_no,
  "members": comFunc.get_all_members,
  "users": comFunc.get_users,
  "vid": comFunc.get_youtube,
  "help": comFunc.get_commands,
  "@": comFunc.make_important_message,
  "decision": comFunc.get_decision,
  "chucknorris": comFunc.get_chuck_norris,
  "giphy": comFunc.get_giphy_gif,
  "advice": comFunc.get_advice,
  "cat": comFunc.get_cat_pic,
  "dog": comFunc.get_dog_pic,
  "fox": comFunc.get_fox_pic,
  'msg': comFunc.handle_notes,
  'stalk': comFunc.get_stalker,
  'quote': comFunc.get_quote,
}