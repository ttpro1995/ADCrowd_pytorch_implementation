from DME_deformable import DMENet, AMGNet

def very_simple_param_count(model):
    result = sum([p.numel() for p in model.parameters()])
    return result

if __name__ == "__main__":
    dme_model = DMENet()
    amg_model = AMGNet()
    dme_count = very_simple_param_count(dme_model)
    amg_count = very_simple_param_count(amg_model)
    # print("dme model ", dme_model)
    print("dme count ", dme_count)
    print("amg count ", amg_count)
