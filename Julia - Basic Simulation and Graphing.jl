using Random
using Statistics
using PyPlot

mutable struct Link
    val::Float64
    exist::Bool
end

probability = parse(Float64, readline())
decoherence = parse(Float64, readline())
num_of_simulation = parse(Int, readline())
final_lambda = Float64[]
time, time_p1, time_p2 = Int[], Int[], Int[]

# DOING SIMULATION
for i in 1:num_of_simulation
    t = 0

    # PHASE 1
    l1 = Link(1, false)
    l2 = Link(1, false)
    while !(l1.exist && l2.exist)
        r1 = rand()
        r2 = rand()
        if l1.exist
            l1.val *= decoherence
        elseif r1 <= probability
            l1.exist = true
        end
        if l2.exist
            l2.val *= decoherence
        elseif r2 <= probability
            l2.exist = true
        end
        t += 1
    end
    push!(time_p1, t)

    # PHASE 2
    l3 = Link(1, false)
    l4 = Link(1, false)
    while !(l3.exist || l4.exist)
        r3 = rand()
        r4 = rand()
        if l3.exist
            l3.val *= decoherence
        elseif r3 <= probability
            l3.exist = true
        end
        if l4.exist
            l4.val *= decoherence
        elseif r4 <= probability
            l4.exist = true
        end
        l1.val *= decoherence
        l2.val *= decoherence
        t += 1
    end
    push!(time_p2, t - time_p1[end])

    # CALCULATING THE FINAL LAMBDA
    if l3.exist
        push!(final_lambda, l1.val * l2.val * l3.val)
    else
        push!(final_lambda, l1.val * l2.val * l4.val)
    end
    push!(time, t)
end

# PLOTTING
fig_1 = figure(figsize=(20, 10))

# LAMBDA DISTRIBUTION
chart_1 = subplot(2, 2, 1)
lambda_val = sort(unique(final_lambda))
lambda_val_count = [count(x -> x == v, final_lambda) for v in lambda_val]
plot(lambda_val, lambda_val_count)
# NAMING
title("The distribution of Lambda Parameter")
xlabel("Lambda Value")
ylabel("Count of Lambda Value")

# TIME DISTRIBUTION
chart_2 = subplot(2, 2, 2)
time_val = sort(unique(time))
time_val_count = [count(x -> x == v, time) for v in time_val]
plot(time_val, time_val_count)
# NAMING
title("The distribution of the Time Until Success")
xlabel("Time to complete")
ylabel("Count of Completion Time")

# The average lambda parameter, given that we succeed at a given time t
chart_3 = subplot(2, 2, 3)
lambda_at_time_t = Dict{Int, Vector{Float64}}()
for (i, e) in enumerate(time)
    if haskey(lambda_at_time_t, e)
        push!(lambda_at_time_t[e], final_lambda[i])
    else
        lambda_at_time_t[e] = [final_lambda[i]]
    end
end
sorted_lambda_at_time_t = sort(collect(lambda_at_time_t))
chart_3_time = Int[]
chart_3_avr_lambda = Float64[]
for (k, v) in sorted_lambda_at_time_t
    push!(chart_3_time, k)
    push!(chart_3_avr_lambda, mean(v))
end
plot(chart_3_time, chart_3_avr_lambda)
# NAMING
title("The average lambda parameter at time t")
xlabel("Time to complete")
ylabel("Average Lambda Value")

# The distribution of lambda given at time t
chart_4 = subplot(2, 2, 4)
time_values = [k for (k, v) in sorted_lambda_at_time_t]
lambda_lists = [v for (k, v) in sorted_lambda_at_time_t]
boxplot(lambda_lists, labels=time_values)
# NAMING
title("Distribution of lambda at time t")
xlabel("Time to complete")
ylabel("Lambda Value")

show()
