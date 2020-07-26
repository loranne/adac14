# Welcome message. Defines a variable for use in subsequent loop.
puts "Welcome to the Audrain County Fair Expenditures Tracker."
party = 0

# Gets user input on how many parties to enter data for. Checks for valid user input. 
loop do
    puts "How many parties visited the fair today? =>"
    break if (party = gets.chomp.to_i).positive? 
    puts "Please enter a positive integer."
end

# Creates empty array for this day at the fair. Array of hashes containing expenditures for each party. Master array.
fair_session = []

# Loop will run the number of times specified by user input in line 4. Each loop (and thereby each party) creates a new hash
# within the array.
party.times do |party_index|
    fair_session[party_index] = {}

    # Asks for user input on how many people in the party.
    loop do
        puts "How many people in Party #{party_index + 1}? => "
        # User input goes into hash, converts input to integer.
        fair_session[party_index][:tix] = gets.chomp.to_i
         # Checks for valid input from user. Breaks loop once input is valid.
        break if (fair_session[party_index][:tix]).positive?
        puts "Please enter a positive number."
    end

    # If statements to determine whether the group discount on 4 tickets applies. 
    if fair_session[party_index][:tix] % 4 == 0
        fair_session[party_index][:tix] = (fair_session[party_index][:tix] / 4 * 112).to_f.round(2)
    elsif fair_session[party_index][:tix] > 4
        fair_session[party_index][:tix] = ((fair_session[party_index][:tix] / 4 * 112) + (fair_session[party_index][:tix] % 4 * 35)).to_f.round(2)
    # If neither of the above conditions are met, the special discounted 4-block price doesn't apply.
    else fair_session[party_index][:tix] = (fair_session[party_index][:tix] * 35).to_f.round(2)
    end

    # Gets user input on cotton candy servings. Loop checks for valid user input, breaks when valid condition is met.
    loop do
        puts "How many servings of cotton candy did they purchase? => "
        fair_session[party_index][:candy] = gets.chomp.to_i
        break if (fair_session[party_index][:candy]) >= 0
        puts "Please enter a positive number."
    end

    # Performs math on user input for cotton candy, converts to float and rounds to 2 decimal places. 
    fair_session[party_index][:candy] = (fair_session[party_index][:candy] * 1.25).to_f.round(2)
        
    puts "How many orders of curly fries did they purchase? => "
    
    # Loop gets user input and checks for valid input. Breaks on good input. 
    loop do
        puts "Large? => "
        fair_session[party_index][:lg_fries] = gets.chomp.to_i
        break if (fair_session[party_index][:lg_fries]) >= 0
        puts "Please enter a valid number."
    end

    # Performs math operations on user input, to get expenditures on fries, as well as function to convert to a float, rounded
    # to 2 decimal places.
    fair_session[party_index][:lg_fries] = (fair_session[party_index][:lg_fries] * 4).to_f.round(2)

    # Loop gts user input on small curly fries, checks for valid input. Breaks on good input. 
    loop do
        puts "Small? => "
        fair_session[party_index][:sm_fries] = gets.chomp.to_i
        break if (fair_session[party_index][:sm_fries]) >= 0
        puts "Please enter a positive number."
    end

    # Math operations on small curly fries user input, to get expenditures on fries. Converts hash entry to float, rounded
    # to 2 decimal places. 
    fair_session[party_index][:sm_fries] = (fair_session[party_index][:sm_fries]).to_f.round(2) * 2.5
end

# Totals all expenses for each party and creates new array containing totals. Converts each total to float, rounded. 
party_total = []
party.times do |party_index|
    party_total[party_index] = (fair_session[party_index][:tix] + fair_session[party_index][:candy] + fair_session[party_index][:lg_fries]+ fair_session[party_index][:sm_fries]).to_f.round(2)
end

# New array for total concessions cost for each party.
party_concession = []
party.times do |party_index|
    party_concession[party_index] = (fair_session[party_index][:candy] + fair_session[party_index][:lg_fries] + fair_session[party_index][:sm_fries]).to_f.round(2)
end 

# Output stating total party costs on tix and concessions, as well as grand total. Loop does this for every party.
party.times do |party_index|
    puts "Party #{party_index+1} spent a total of $%0.2f on tickets and $%0.2f on concessions, for a total of $%0.2f." % [fair_session[party_index][:tix], party_concession[party_index], party_total[party_index]]
end

# Totals up fair earnings across all parties. 
fair_earnings = 0
party_total.each do |subtotal|
    fair_earnings = fair_earnings + subtotal
end

# String formatting in order to get a sensible printout of monetary value, rather than string interpolation. 
puts "Today the fair earned a total of $%0.2f." % [fair_earnings]

# Totals up all concessions expenditures across all parties. Print's fair's total concessions earnings for the session.
fair_concession = 0
party_concession.each do |food_total|
    fair_concession = fair_concession + food_total
end
puts "All parties today spent a total of $%0.2f on concessions." % [fair_concession]

# Determines highest spending party. Outputs that party's number and total spent by that party.
max = party_total[0]
big_party = 0
party_total.length.times do |party_index|
    if party_total[party_index] > max 
        max = party_total[party_index]
        big_party = party_index + 1
    end
end
puts "Party #{big_party} spent the most, with a grand total of $%0.2f." % [max]
