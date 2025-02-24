
# Функции обновления состояния

# функция обновления добавление новых пользователей
def s_new_video(params,substep,state_history,previous_state,policy_input):

    updated_new_video = params['new_video_month']
    return 'new_video', updated_new_video

# функция обновления добавление новых пользователей
def s_all_video(params,substep,state_history,previous_state,policy_input):

    updated_all_video = previous_state['all_video']+params['new_video_month']
    return 'all_video', updated_all_video


# функция обновления добавление новых пользователей
def s_month(params,substep,state_history,previous_state,policy_input):

    updated_month = previous_state['month']+1
    return 'month', updated_month


# функция обновления добавление новых пользователей
def s_new_view(params,substep,state_history,previous_state,policy_input):

    updated_view = policy_input['new_new_view']
    return 'new_view', updated_view



# функция обновления добавление новых пользователей
def s_all_view(params,substep,state_history,previous_state,policy_input):

    updated_all_view = previous_state['all_view'] + policy_input['new_all_view'] +  previous_state['second_view'] 
    return 'all_view', updated_all_view

# функция обновления добавление новых пользователей
def s_count_view(params,substep,state_history,previous_state,policy_input):

    updated_all_view = previous_state['new_video']*previous_state['new_view'] +  previous_state['second_view'] 
    return 'count_view', updated_all_view


# функция обновления добавление новых пользователей
def s_second_view(params,substep,state_history,previous_state,policy_input):

    updated_all_view = policy_input['new_second_view']
    return 'second_view', updated_all_view

# функция обновления добавление новых пользователей
def s_formula(params,substep,state_history,previous_state,policy_input):

    updated_all_view = policy_input['new_formula']
    return 'formula', updated_all_view

# функция обновления добавление новых пользователей
def s_subscriber(params,substep,state_history,previous_state,policy_input):

    updated_all_view = previous_state['count_view']*0.01+previous_state['subscribers']
    return 'subscribers', updated_all_view

# функция обновления добавление новых пользователей
def s_buks(params,substep,state_history,previous_state,policy_input):

    cpm = params['cpm']

    updated_all_view = previous_state['count_view']*cpm/1000
    return 'buks', updated_all_view





# функция обновления добавление новых пользователей
def s_k_grow(params,substep,state_history,previous_state,policy_input):

    updated_k_grow = policy_input['new_k_grow']
    return 'k_grow', updated_k_grow