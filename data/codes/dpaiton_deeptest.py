import osimport caffeimport numpy as npfrom scipy.misc import imsavefrom skimage import img_as_ubytefrom skimage.transform import rescaleimport IPython
#style_file = "images/style/starry_night.jpg"style_file = "images/style/monet_soleil_levant.jpg"#content_file = "images/content/sanfrancisco.jpg"content_file = "images/content/venice_night.jpg"
solver_file = "models/deepstyle/solver.prototxt"proto_file = "models/deepstyle/deepstyle_merge_gen.prototxt"
model_file = "models/deepstyle/deepstyle_merge_gen.caffemodel"mean_file = "models/deepstyle/ilsvrc_2012_mean.npy"
length = 128#512
img_style = caffe.io.load_image(style_file)img_content = caffe.io.load_image(content_file)
#net = caffe.Net(proto_file, model_file, caffe.TEST)solver = caffe.SGDSolver(solver_file)net = solver.netnet.copy_from(model_file)
# assume that convnet input is squareorig_style_dim = min(net.blobs["style_data"].shape[2:])orig_content_dim = min(net.blobs["content_data"].shape[2:])
# rescale the imagesscale = max(length / float(max(img_style.shape[:2])),            orig_style_dim / float(min(img_style.shape[:2])))img_style = rescale(img_style, scale)
scale = max(length / float(max(img_content.shape[:2])),            orig_content_dim / float(min(img_content.shape[:2])))img_content = rescale(img_content, scale)
new_dims = (1, img_style.shape[2]) + img_style.shape[:2]net.blobs["style_data"].reshape(*new_dims)
new_dims = (1, img_content.shape[2]) + img_content.shape[:2]net.blobs["content_data"].reshape(*new_dims)net.blobs["content_bias"].reshape(*new_dims)
transformer = caffe.io.Transformer({"style_data": net.blobs["style_data"].data.shape, \ "content_data": net.blobs["content_data"].data.shape})transformer.set_mean("style_data", np.load(mean_file).mean(1).mean(1))transformer.set_channel_swap("style_data", (2,1,0))transformer.set_transpose("style_data", (2,0,1))transformer.set_raw_scale("style_data", 255)transformer.set_mean("content_data", np.load(mean_file).mean(1).mean(1))transformer.set_channel_swap("content_data", (2,1,0))transformer.set_transpose("content_data", (2,0,1))transformer.set_raw_scale("content_data", 255)
style_in = transformer.preprocess("style_data", img_style)content_in = transformer.preprocess("content_data", img_style)
net.blobs["style_data"].data[0] = style_innet.blobs["content_data"].data[0] = content_in
solver.solve()
out_data = net.blobs["content_bias"].dataout_img = transformer.deprocess("content_data", out_data)
imsave("images/generated/gen_test.jpg", out_img)
IPython.embed()